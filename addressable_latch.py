from machine import Pin

class AddressableLatch:
    def __init__(self, A : int , B : int, C : int, D : int, ENABLE: list = [], debug = False):
        self.A = Pin(A, mode=Pin.OUT)
        self.B = Pin(B, mode=Pin.OUT)
        self.C = Pin(C, mode=Pin.OUT)
        self.D = Pin(D, mode=Pin.OUT)
        self.NUMBER_OF_ICS = len(ENABLE)
        self.E_pins = [Pin(E, mode=Pin.OUT) for E in ENABLE]
        self.DEBUG : bool = debug

    def debug_print(self, text : str):
        """Prints debug statements."""
        if self.DEBUG:
            print(text)

    
    def switcher(self, ic_index: int):
        """Enables the ic that has the needed latch."""
        self.debug_print(f"Switching ic #{ic_index}")
        
        #Creates a list of disabled ics enable pins 
        disabled_ics = [E for index, E in enumerate(self.E_pins) if not index == ic_index]
        self.debug_print(f"Disabled ics: {disabled_ics}")

        #Disables the ics by switching the enable pin high (memory hold mode).
        for d in disabled_ics:
            self.debug_print(d)          
            d.value(1)

        enabled = self.E_pins[ic_index]
        enabled.value(0)
        return enabled

    def output(self, latch_number : int, output_state : int):
        """Outputs a state to a specified latch in one of the ics."""

        #latch_number // 8 Calculates the index of the ic that has the latch number.
        enabled = self.switcher(latch_number // 8)
        
        #Calculates the the latch index in said ic (each ic holding 8 latches).
        latch_number = latch_number % 8
        self.debug_print(f"current latch ic {latch_number}")

        #Turns the latch number to binary to distribute the first three bits to control the specific latch.
        binary = bin(latch_number).replace('0b','00')
        self.A.value(int(binary[-1]))
        self.B.value(int(binary[-2]))
        self.C.value(int(binary[-3]))
        self.D.value(output_state)

        #Disables ic (memory hold mode) after use.
        enabled.value(1)
    
    def clear(self):
        """Clears A, B, C, D pins."""
        clear_list = [self.A, self.B, self.C, self.D]
        for pin in clear_list:
            pin.value(0)
        
    def disable_all(self):
        """Disables all ics."""
        for E in self.E_pins:
            E.value(1)
        self.clear()
