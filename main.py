import os
from functions.functions_menu import pre_process_data, create_time_sires, anilisis_time_siris, forecasting

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        if not os.path.exists("data/new_data/"):
            os.mkdir('data/new_data/')
        t = 'D'
        flag_show_plot = True
        print("1. Process the data in data/online_retail_||(2).csv")
        print("2. Make time sires from new data of menu option 1 result")
        print("3. Analyze time sires which was make in second option")
        print("4. Forecast time sires from option 2")
        print("5. Settings")
        print("0. Exit")
        choice = int(input("Input number: "))
        if choice == 1:
            print('Process started')
            pre_process_data()
            print('Finished')
        elif choice == 2:
            print('Process started')
            create_time_sires()
            print('Finished')
        elif choice == 3:
            print('Process started')
            anilisis_time_siris(t=t, flg_print=flag_show_plot)
            print('Finished')
        elif choice == 4:
            print('Process started')
            forecasting(t=t)
            print('Finished')
        elif choice == 5:
            print('t: ', t)
            print('Show plot: ', flag_show_plot)
        elif choice == 0:
            break
        else:
            print('Wrong input')
        input("Press Enter to continue...")
        os.system('cls')


