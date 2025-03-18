from asgiref.sync import sync_to_async
import asyncio
from django.db import connections
from datetime import timedelta
from django.utils import timezone
from .models import AttendanceShortTerm, AttendanceLongTerm

class DatabaseMonitor:
    def __init__(self, check_interval=5):  # Check every 5 seconds by default
        self.check_interval = check_interval
        self.is_running = False

    async def start_monitoring(self):
        self.is_running = True
        while self.is_running:
            await self.check_database_consistency()
            await asyncio.sleep(self.check_interval)

    async def check_database_consistency(self):
        try:
            # Get all unprocessed records from both databases
            short_term_records = await sync_to_async(list)(
                AttendanceShortTerm.objects.filter(processed=False)
            )
            long_term_records = await sync_to_async(list)(
                AttendanceLongTerm.objects.filter(processed=False)
            )

            # Check for matching records
            for short_record in short_term_records:
                for long_record in long_term_records:
                    if self._records_match(short_record, long_record):
                        print(f"Matching records found for {short_record.name}")
                        # Mark records as processed
                        short_record.processed = True
                        long_record.processed = True
                        await sync_to_async(short_record.save)()
                        await sync_to_async(long_record.save)()

        except Exception as e:
            print(f"Error in database monitoring: {e}")

    def _records_match(self, short_record, long_record):
        return (
            short_record.name == long_record.name and
            short_record.phone_number == long_record.phone_number and
            abs(short_record.timestamp - long_record.timestamp) < timedelta(seconds=1)
        )

    def stop_monitoring(self):
        self.is_running = False