#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct
{
    char username[50];
    int status;
    int balance;
    void (*play_blackjack)(struct Player *);
    void (*play_roulette)(struct Player *);
    void (*high_stakes_dice)(struct Player *);
} Player;

typedef struct
{
    char username[88];
} Dev;

int main();
void developer_mode(Player *player);

int draw_card()
{
    return rand() % 11 + 1;
}

void wait_for_keypress()
{
    printf("Press any key to continue...\n");
    while (getchar() != '\n');
    getchar();
}

void play_blackjack(Player *player)
{
    if (!player) {
        printf("Error: Player data is not available.\n");
        return;
    }
    
    int choice;
    
    while (1)
    {
        printf("--------------------\nWhat would you like to do?\n");
        printf("[1] Play Blackjack\n[2] Quit\n>: ");

        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a number.\n");
        }

        if (choice == 1) {
            printf("--------------------\nWelcome to Blackjack, %s!\n", player->username);
            
            int bet;
            
            printf("Enter your bet (current balance: %d): ", player->balance);
            if (scanf("%d", &bet) != 1 || bet > player->balance || bet <= 0) {
                printf("Invalid bet.\n");
            }

            int player_total = draw_card() + draw_card();
            int dealer_total = draw_card() + draw_card();
            int player_card_count = 2;
            int dealer_card_count = 2;

            printf("Your total: %d\n", player_total);
            printf("Dealer's visible card: %d\n", dealer_total % 10);

            wait_for_keypress();

            while (player_total < 21)
            {
                printf("--------------------\nWhat would you like to do?\n");
                printf("[1] Hit\n[2] Stand\n[3] Double Down\n>: ");
                
                
                if (scanf("%d", &choice) != 1) {
                    printf("Invalid input.\n");
                }

                if (choice == 1) {
                    player_total += draw_card();
                    player_card_count++;
                    printf("You drew a card. Your total is now %d.\n", player_total);
                    wait_for_keypress();
                }
                else if (choice == 2) {
                    break;
                }
                else if (choice == 3 && bet * 2 <= player->balance) {
                    bet *= 2;
                    player_total += draw_card();
                    player_card_count++;
                    printf("You doubled down! Your total is now %d.\n", player_total);
                    wait_for_keypress();
                    break;
                }
                else {
                    printf("Invalid option. Please choose again.\n");
                }

                if (player_total > 21) {
                    printf("Your total went over 21. You lose!\n");
                    player->balance -= bet;
                    printf("Your new balance is: %d\n", player->balance);
                    wait_for_keypress();
                    break;
                }
            }

            printf("Dealer's total: %d\n", dealer_total);
            
            while (dealer_total < 17)
            {
                dealer_total += draw_card();
                dealer_card_count++;
                printf("Dealer draws a card. Dealer's total is now %d.\n", dealer_total);
                wait_for_keypress();
            }

            if (player_total <= 21) {
                if (dealer_total > 21) {
                    printf("Dealer busts! You win!\n");
                    player->balance += bet;
                }
                else if (player_total > dealer_total) {
                    printf("You win!\n");
                    player->balance += bet;
                }
                else if (player_total < dealer_total) {
                    printf("You lose!\n");
                    player->balance -= bet;
                }
                else {
                    printf("It's a tie!\n");
                }
                wait_for_keypress();
                printf("Your new balance is: %d\n", player->balance);
            }
        }
        else if (choice == 2) {
            printf("Exiting the Blackjack room. Goodbye!\n");
            break;
        }
        else {
            printf("Invalid option. Please choose again.\n");
        }
    }
}

void change_username(Player *player)
{
    printf("previous username: %s\n", player->username);
    printf("Enter your new username: ");
    scanf("%s", player->username);
}

void show_admin_key(void)
{
    system("cat flag.txt");
}

void play_roulette(Player *player)
{
    if (!player) {
        printf("Error: Player data is not available.\n");
        return;
    }

    int choice;

    while (1)
    {
        printf("--------------------\nWhat would you like to do?\n");
        printf("[1] Play Roulette\n[2] Quit\n>: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("--------------------\nWelcome to Roulette, %s!\n", player->username);
            
            int bet;
            
            printf("Enter your bet (current balance: %d): ", player->balance);
            scanf("%d", &bet);

            if (bet > player->balance || bet <= 0) {
                printf("Invalid bet.\n");
                break;
            }

            int bet_choice;
            
            printf("--------------------\nWhat do you want to bet on?\n");
            printf("[1] A number (0-36)\n");
            printf("[2] Red or Black\n");
            printf("[3] Both (Number and Color)\n>: ");
            
            
            scanf("%d", &bet_choice);

            int chosen_number = -1;
            char chosen_color[10] = "";

            if (bet_choice == 1 || bet_choice == 3) {
                printf("Choose a number between 0 and 36: ");
                scanf("%d", &chosen_number);

                if (chosen_number < 0 || chosen_number > 36) {
                    printf("Invalid number.\n");
                    break;
                }
            }

            if (bet_choice == 2 || bet_choice == 3) {
                printf("Choose a color (red/black): ");
                scanf("%s", chosen_color);

                if (strcasecmp(chosen_color, "red") != 0 && strcasecmp(chosen_color, "black") != 0) {
                    printf("Invalid color.\n");
                    break;
                }
            }

            int roulette_number = rand() % 37;
            char roulette_color[10];

            if (roulette_number == 0) {
                strcpy(roulette_color, "green");
            }
            else if ((roulette_number >= 1 && roulette_number <= 10) || (roulette_number >= 19 && roulette_number <= 28)) {
                if (roulette_number % 2 == 0)
                    strcpy(roulette_color, "black");
                else
                    strcpy(roulette_color, "red");
            }
            else {
                if (roulette_number % 2 == 0)
                    strcpy(roulette_color, "red");
                else
                    strcpy(roulette_color, "black");
            }

            printf("The roulette landed on: %d (%s)\n", roulette_number, roulette_color);

            int win = 0;

            if (bet_choice == 1 || bet_choice == 3) {
                if (chosen_number == roulette_number) {
                    printf("You win on your number bet!\n");
                    player->balance += bet * 35;
                    win = 1;
                }
            }

            if (bet_choice == 2 || bet_choice == 3) {
                if (strcasecmp(chosen_color, roulette_color) == 0) {
                    printf("You win on your color bet!\n");
                    player->balance += bet;
                    win = 1;
                }
            }

            if (!win) {
                printf("You lose!\n");
                player->balance -= bet;
            }
            wait_for_keypress();
            printf("Your new balance is: %d\n", player->balance);
        }
        else if (choice == 2) {
            printf("Exiting the Roulette room. Goodbye!\n");
            break;
        }
        else {
            printf("Invalid option. Please choose again.\n");
        }
    }
}

void assign_dev_username()
{
    Dev *dev = malloc(sizeof(Dev));

    printf("Welcome dev, enter your new username: ");
    scanf("%s", dev->username);
}

void high_stakes_dice(Player *player)
{
    if (!player) {
        printf("Error: Player data is not available.\n");
        return;
    }

    int choice;
    while (1)
    {
        printf("--------------------\nWhat would you like to do?\n");
        printf("[1] Play High-Stakes Dice\n[2] Quit\n>: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("--------------------\nWelcome to High-Stakes Dice, %s!\n", player->username);

            int bet;
            
            printf("Enter your bet (current balance: %d): ", player->balance);
            scanf("%d", &bet);

            if (bet > player->balance || bet <= 0) {
                printf("Invalid bet.\n");
                break;
            }

            int player_roll = rand() % 6 + 1;
            int house_roll = rand() % 6 + 1;

            printf("Your roll: %d\nHouse roll: %d\n", player_roll, house_roll);
            
            if (player_roll > house_roll) {
                printf("You win!\n");
                player->balance += bet * 2;
            }
            else if (player_roll < house_roll) {
                printf("You lose!\n");
                player->balance -= bet;
            }
            else {
                printf("It's a tie! No money won or lost.\n");
            }
            wait_for_keypress();
            printf("Your new balance is: %d\n", player->balance);
        }
        else if (choice == 2) {
            printf("Exiting the High-Stakes Dice room. Goodbye!\n");
            break;
        }
        else {
            printf("Invalid option. Please choose again.\n");
        }
    }
}

void enter_vip_room(Player *player)
{
    if (player->balance >= 1000000) {
        printf("--------------------\nWelcome to the VIP Room, %s!\n", player->username);

        player->high_stakes_dice = high_stakes_dice;

        int choice;
        while (1) 
        {
            printf("\n--------------------\nVIP Menu:\n[1] Change Username\n[2] Play VIP Blackjack\n[3] Play VIP Roulette\n[4] Play High-Stakes Dice\n[5] Developer Mode\n[6] Exit VIP Room\n>: ");
            scanf("%d", &choice);

            switch (choice)
            {
            case 1:
                change_username(player);
                break;
            case 2:
                player->play_blackjack(player);
                break;
            case 3:
                player->play_roulette(player);
                break;
            case 4:
                player->high_stakes_dice(player);
                break;
            case 5:
                developer_mode(player);
                break;
            case 6:
                printf("Exiting VIP Room...\n");    
                return;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
            }
        }
    }
    else {
        printf("Sorry, %s. You need to be a millionaire to enter the VIP Room.\n", player->username);
    }
}


void developer_mode(Player *player)
{
    if (player->status == 0xcafebabe) {
        int n;

        while (1)
        {
            printf("\n--------------------\nmy bosses don't have any empathy for my health!\n[1] assign a username to the developer\n[2] show main() address\n[3] delete player\n[4] quit developer menu\n>: ");
            scanf("%d", &n);
            
            switch (n) 
            {
            case 1:
                assign_dev_username();
                break;
            case 2:
                printf("[debug] main(): %p\n", main);
                break;
            case 3:
                printf("Deleted [%s] => final balance was: %d\n", player->username, player->balance);
                free(player);
                break;
            case 4:
                printf("bye!!!\n");
                return;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
            }
        }
    }
    else {
        printf("Only developers can enter the developer mode !\n");
        
    }
}

int main()
{
    srand(time(NULL));
    
    setvbuf(stdout, NULL, _IONBF, 0);
    
    Player *player = malloc(sizeof(Player));

    printf("Enter your username: ");
    scanf("%s", player->username);
    
    player->status = 0;
    player->balance = 1337;

    player->play_blackjack = play_blackjack;
    player->play_roulette = play_roulette;

    int choice;

    while (1)
    {
        if (player->balance <= 0) {
            printf("You're bankrupt get out of here!\n");
            return 0;
        }
        
        printf("\n--------------------\nWelcome to the casino!\nMenu:\n[1] Change Username\n[2] Play Blackjack\n[3] Play Roulette\n[4] VIP Room\n[5] Exit\n>: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            change_username(player);
            break;
        case 2:
            player->play_blackjack(player);
            break;
        case 3:
            player->play_roulette(player);
            break;
        case 4:
           enter_vip_room(player);
            break;
        case 5:
            printf("Goodbye, %s! Your final balance is: %d\n", player->username, player->balance);
            free(player);
            return 0;
        default:
            printf("Invalid choice. Please try again.\n");
            break;
        }
    }
    return 0;
}