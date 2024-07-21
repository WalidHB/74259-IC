# 74259-IC
A MicroPython single file library for controlling 74259 addressable latches across multiple ICs. This library allows you to select ICs using enable pins while sharing common set and output state pins.

## Requirements

- **MicroPython**

## Features

- **Control Multiple ICs**: Manage latches by enabling specific ICs.
- **Pin Configuration**: Share common set and output state pins among ICs.
- **Debugging**: Optional debug output.

## Installation

To use this library, copy the `addressable_latch.py` file to your MicroPython environment.

## Example Usage

```
from machine import Pin
from addressable_latch import AddressableLatch

# Initialize AddressableLatch with pin numbers
latch = AddressableLatch(A=0, B=1, C=2, D=3, ENABLE=[4, 5, 6], debug=True)

# Set latch 1 on IC 1 to high (array indexing starting from 0)
latch.output(latch_number=9, output_state=1)

# Clear all A, B, C, D pins
latch.clear()

# Disable all ICs
latch.disable_all()```
