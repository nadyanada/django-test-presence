from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AttendanceShortTerm, AttendanceLongTerm
from .forms import AttendanceForm
from asgiref.sync import sync_to_async
import asyncio
import threading
import time

async def attendance_form(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if await sync_to_async(form.is_valid)():
            short_term_record = await sync_to_async(form.save)()
            
            long_term_record = await sync_to_async(AttendanceLongTerm.objects.create)(
                name=short_term_record.name,
                phone_number=short_term_record.phone_number,
                timestamp=short_term_record.timestamp
            )

            print(f"Created records - Short term: {short_term_record.id}, Long term: {long_term_record.id}")
            return redirect('verify')
    else:
        form = AttendanceForm()
    
    return await sync_to_async(render)(request, 'attendance_form.html', {'form': form})

async def verify_view(request):
    return await sync_to_async(render)(request, 'verify.html')

async def success_view(request):
    await sync_to_async(messages.success)(request, 'Your attendance has been successfully recorded!')
    return await sync_to_async(render)(request, 'success.html')