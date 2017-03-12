#!/bin/bash
echo $(expr $(cat /sys/class/backlight/acpi_video0/brightness) + 1) | tee /sys/class/backlight/acpi_video0/brightness