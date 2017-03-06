
int redPin = 10;
int samp = 10;
int light_on = 100;
int temp_red=0;
int temp_ir=0;
int red_val=0;
int ir_val=0;

void setup() {
  // nothing happens in setup
  Serial.begin(9600);
  analogReference(INTERNAL);
}

void loop() {
      
      // turn on red light which turns off IR light
      analogWrite(redPin, 255);
      temp_red=0;
      for (int ti = 0 ; ti <= light_on; ti+= samp){
        temp_red+=analogRead(A0);
        delay(samp);
      }
      
      red_val = temp_red/((light_on/samp)+1);
      //Serial.println(red_val);
      //Serial.println(5);


      // turn off red light which turns on IR light
      analogWrite(redPin,0);
      temp_ir=0;
      for (int ti = 0 ; ti <= light_on; ti+= samp){
        temp_ir+=analogRead(A0);
        delay(samp);
      }

      //Serial.println(ir_val);
      //Serial.println(25);
      
    ir_val = temp_ir/((light_on/samp)+1);
    float ratio = float(red_val)/float(ir_val);
    
    String out_val = String(red_val, DEC)+','+String(ir_val, DEC)+','+String(ratio, DEC);

    //Serial.println(out_val);
    Serial.println(ratio);
    
  }

