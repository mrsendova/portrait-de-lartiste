/* I2C LCD 16x2 Arduino Tutorial
 * More info http://www.ardumotive.com/i2clcd(en).html
 * Dev: Michalis Vasilakis Date: 19/11/2016 Ver. 1.0 */

//Libraries 
#include <Wire.h>  
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Set the LCD I2C address, if it's not working try 0x27.

void setup(){
  lcd.init();
  lcd.begin(16,2);   // iInit the LCD for 16 chars 2 lines
  lcd.backlight();   // Turn on the backligt (try lcd.noBaklight() to turn it off)
  lcd.setCursor(0,0); //First line
  lcd.print("La Machine  v0.2");
  lcd.setCursor(0,1);
  lcd.print("Appuyez calculer");
}

void loop(){

}
