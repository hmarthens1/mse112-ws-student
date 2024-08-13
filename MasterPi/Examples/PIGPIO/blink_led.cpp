#include <iostream>
#include <pigpio.h>
#include <unistd.h>  // For sleep functions

#define LED_PIN 17  // GPIO pin where the LED is connected

int main()
{
    // Initialize the pigpio library
    if (gpioInitialise() < 0)
    {
        std::cerr << "pigpio initialization failed." << std::endl;
        return 1;
    }

    // Set the LED pin as an output
    gpioSetMode(LED_PIN, PI_OUTPUT);

    // Blink the LED
    try
    {
        while (true)
        {
            gpioWrite(LED_PIN, 1);  // Turn LED on
            sleep(1);               // Wait for 1 second
            gpioWrite(LED_PIN, 0);  // Turn LED off
            sleep(1);               // Wait for 1 second
        }
    }
    catch (...)
    {
        // Clean up on exception
        gpioWrite(LED_PIN, 0);  // Turn LED off
        gpioTerminate();        // Terminate the pigpio library
        std::cout << "Program terminated" << std::endl;
    }

    // Clean up on normal exit (though the code above is an infinite loop)
    gpioTerminate();
    return 0;
}
