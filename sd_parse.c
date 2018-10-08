#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef u_int8_t uint8_t;

int main(int argc, char *argv[]){

  if (argc != 2){
    printf("Please supply one file name.\n");
    exit(1);
  }

  FILE *datafile_pointer;

  if ((datafile_pointer = fopen(argv[1], "r"))==NULL) {
    printf("Cannot open file.\n");
    exit(1);
  }

  FILE *alti_t_pointer;
  FILE *alti_p_pointer;
  FILE *accel_x_pointer;
  FILE *accel_y_pointer;
  FILE *accel_z_pointer;
  alti_t_pointer  = fopen("alti_t.txt", "w");
  alti_p_pointer  = fopen("alti_p.txt", "w");
  accel_x_pointer = fopen("accel_x.txt", "w");
  accel_y_pointer = fopen("accel_y.txt", "w");
  accel_z_pointer = fopen("accel_z.txt", "w");

  uint8_t descriptor;
  int8_t accel[6];
  int8_t alti[6];
  while(fread(&descriptor, 1, 1, datafile_pointer)){
    if (descriptor == 0xAA){
      if ((fread(accel, 1, 6, datafile_pointer)) == 6){
        fprintf(accel_x_pointer, "%d,", (((int)accel[1] <<8)|accel[0]));
        fprintf(accel_y_pointer, "%d,", (((int)accel[3] <<8)|accel[2]));
        fprintf(accel_z_pointer, "%d,", (((int)accel[5] <<8)|accel[4]));
      }
      else {
        break;
      }
    } else if (descriptor == 0x55){
      if ((fread(alti, 1, 5, datafile_pointer)) == 5){
        fprintf(alti_p_pointer, "%d,", (((((int)alti[0] <<8) | alti[1]) <<8) | alti[2]));
        fprintf(alti_t_pointer, "%d,", (((int)alti[3] <<8) | alti[4]));
      }
      else {
        break;
      }

    } else {
      //pass character
    }
  }

  fprintf(alti_t_pointer, "0");
  fprintf(alti_p_pointer, "0");
  fprintf(accel_x_pointer, "0");
  fprintf(accel_y_pointer, "0");
  fprintf(accel_z_pointer, "0");
  fclose(datafile_pointer);
  fclose(alti_t_pointer);
  fclose(alti_p_pointer);
  fclose(accel_x_pointer);
  fclose(accel_y_pointer);
  fclose(accel_z_pointer);

  return 0;
}
