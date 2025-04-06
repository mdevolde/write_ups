undefined8 main(void)

{
  long in_FS_OFFSET;
  int local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_14 = 0;
  do {
    while( true ) {
      puts(
          "<-. (-\')                (-\')  _  (-\')          \n \\(OO )_      .->   <-.(OO )  \\- .(OO )    .->   \n ,--./  ,-.) ,--.\'  ,-.,------,) _.\'    \\ ,---(-\')\n |   .\'   |( -\')\'.\'  /|   /. \'(_...--\'\'\'  .-(OO )\n |  |\'.\'|  |(OO \\    / |  |_.\' ||  |_.\'  ||  | .-, \\\n |  |   |  | |  /   /) |  .   .\'|  .___.\'|  | \'.(_/\n |  |   |  | -/   /  |  |\\  \\ |  |     |  \'-\'  | \n --\'   --\'   --\'    --\' \'--\'--\'      -- ---\'  "
          );
      display_main_menu();
      printf("# Choose > ");
      fflush(stdout);
      __isoc99_scanf(&DAT_00402122,&local_14);
      if (local_14 == 3) {
        if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
          return 0;
        }
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      if (local_14 < 4) break;
LAB_00401c69:
      puts("# Invalid Input");
      sleep(1);
      printf("\x1b[1;1H\x1b[2J");
      fflush(stdout);
    }
    if (local_14 == 1) {
      intro();
    }
    else {
      if (local_14 != 2) goto LAB_00401c69;
      wip();
    }
  } while( true );
}

void display_main_menu(void)

{
  puts("#########[Main Menu]#########");
  puts("#       1) New Game         #");
  puts("#       2) Load Game        #");
  puts("#       3) Exit             #");
  puts("#############################");
  return;
}

void intro(void)

{
  printf("\x1b[1;1H\x1b[2J");
  fflush(stdout);
  print_dialogue("# You wake up in a dark cave.");
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  print_dialogue(
                "\n# Not far in front of you, you see a dimly lit hooded figure standing between two  entrances.\n"
                );
  sleep(1);
  print_dialogue("# One on his left, one on his right...\n");
  sleep(1);
  print_dialogue("# Behind you, a glimmer of daylight.");
  sleep(1);
  print_dialogue(" Probably an exit.\n");
  sleep(1);
  print_dialogue("# What do you do?\n");
  sleep(1);
  new_game();
  return;
}

void print_dialogue(char *param_1)

{
  size_t sVar1;
  uint local_10;
  
  sVar1 = strlen(param_1);
  for (local_10 = 0; local_10 < (uint)sVar1; local_10 = local_10 + 1) {
    putchar((int)param_1[local_10]);
    fflush(stdout);
    usleep(20000);
  }
  return;
}

void new_game(void)

{
  long in_FS_OFFSET;
  int local_5c;
  undefined1 local_58 [24];
  undefined1 *local_40;
  undefined1 local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_40 = local_38;
  local_5c = 0;
LAB_0040196f:
  display_menu_1();
  printf("# Choose > ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00402122,&local_5c);
  getchar();
  if (local_5c == 4) {
    print_dialogue("# You managed to exit the cave.\n");
    if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
      return;
    }
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  if (local_5c < 5) {
    if (local_5c == 3) {
      right_entrance(1);
      goto LAB_0040196f;
    }
    if (local_5c < 4) {
      if (local_5c == 1) {
        talk(local_40);
      }
      else {
        if (local_5c != 2) goto LAB_00401a2f;
        left_entrance(local_40,local_58);
      }
      goto LAB_0040196f;
    }
  }
LAB_00401a2f:
  puts("# Invalid Input");
  goto LAB_0040196f;
}

void display_menu_1(void)

{
  puts("\n[Action Menu]##################");
  puts(" 1) Talk to the hooded figure #");
  puts(" 2) Follow the left path      #");
  puts(" 3) Follow the right path     #");
  puts(" 4) Try to exit the cave      #");
  puts("###############################");
  return;
}

void right_entrance(int param_1)

{
  if (param_1 == 1) {
    wip();
    puts(
        "[DEBUG] Maybe I could use system() to do cool weird things on the computer. Breaking the fo urth wall."
        );
    fflush(stdout);
  }
  else {
    system("/bin/sh");
  }
  return;
}

void talk(char *param_1)

{
  print_dialogue("# You approach the hooded figure...\n");
  sleep(1);
  print_dialogue("# What do you say?\n");
  printf("# > ");
  fflush(stdout);
  fgets(param_1,0x28,stdin);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  print_dialogue("\n# No answer...\n");
  return;
}

void left_entrance(undefined8 param_1,undefined8 param_2)

{
  long in_FS_OFFSET;
  undefined1 local_15;
  int local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_15 = 0;
  local_14 = 0;
  print_dialogue("# You take the left entrance and venture deeper into the cave.");
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  print_dialogue("\n# In the darkness you glimpse at the shape of a great beast.\n");
  sleep(1);
  print_dialogue("# It seems like it noticed you and slowly starts coming towards you.");
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  putchar(0x2e);
  fflush(stdout);
  sleep(1);
  print_dialogue("\n# What do you do?\n");
LAB_00401655:
  do {
    display_menu_2();
    printf("# Choose > ");
    fflush(stdout);
    __isoc99_scanf(&DAT_00402122,&local_14);
    getchar();
    if (local_14 == 4) {
      print_dialogue("# You managed to go back.\n");
      if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (local_14 < 5) {
      if (local_14 == 3) {
        print_dialogue("# The beast accelerates towards you...\n");
        sleep(0);
        print_dialogue("# It hits you.\n");
        sleep(1);
        print_dialogue("# You died.\n");
                    /* WARNING: Subroutine does not return */
        exit(0);
      }
      if (local_14 < 4) {
        if (local_14 == 1) {
          print_dialogue("# You are not strong enough.\n");
          sleep(1);
          print_dialogue("# You died.\n");
                    /* WARNING: Subroutine does not return */
          exit(0);
        }
        if (local_14 == 2) {
          shout(param_1,param_2,&local_15);
          goto LAB_00401655;
        }
      }
    }
    puts("# Invalid Input");
  } while( true );
}

void display_menu_2(void)

{
  puts("\n[Action Menu]##################");
  puts(" 1) Fight the beast           #");
  puts(" 2) Shout at the beast        #");
  puts(" 3) Do nothing                #");
  puts(" 4) Go back                   #");
  puts("###############################");
  return;
}

void shout(long param_1,char *param_2,char *param_3)

{
  size_t sVar1;
  long in_FS_OFFSET;
  uint local_40;
  uint local_3c;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (*param_3 != '\0') {
    print_dialogue("# It hits you.\n");
    sleep(1);
    print_dialogue("# You died.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  print_dialogue("# What do you shout?\n");
  printf("# > ");
  fflush(stdout);
  fgets(param_2,0x18,stdin);
  sprintf(local_38,"# You shout %s",param_2);
  print_dialogue(local_38);
  sleep(1);
  sVar1 = strlen(param_2);
  printf("%d",sVar1);
  fflush(stdout);
  local_40 = 0;
  do {
    if (0x18 < local_40) {
LAB_0040145e:
      if (*param_3 == '\x01') {
        print_dialogue("\n# The beast shouts back some cryptic numbers...\n#");
        for (local_3c = 0; (local_3c < 0x19 && (*(char *)(param_1 + (ulong)local_3c) != '\0'));
            local_3c = local_3c + 1) {
          printf(" %d",(ulong)(uint)(int)param_2[local_3c]);
          fflush(stdout);
          usleep(250000);
        }
        usleep(250000);
        print_dialogue("\n# The beast accelerates towards you...\n");
      }
LAB_0040152f:
      if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    param_2[local_40] = param_2[local_40] - *(char *)(param_1 + (ulong)local_40);
    if (*(char *)(param_1 + (ulong)local_40) == '\0') {
      if (*param_3 == '\0') {
        print_dialogue("\n# The beast stops...\n");
        wip();
        goto LAB_0040152f;
      }
      goto LAB_0040145e;
    }
    if (param_2[local_40] != '\0') {
      *param_3 = '\x01';
    }
    local_40 = local_40 + 1;
  } while( true );
}

void wip(void)

{
  puts("[!] WIP : This part is not finished.");
  fflush(stdout);
  return;
}
