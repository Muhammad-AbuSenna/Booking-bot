# Please Note:
# This robot was made 1 year ago from puplishing this project.
# some functions is not reliable rightnow duo to the Website UI changes.
# I haven't included so much error handling to this project cuse it's just a demo not a production product.
# Thank You for understandin ^_^ .


from booking.booking import Booking

try:
    with Booking(teardown=False) as bot:
        print(
            "Hey there, I'm your booking bot\n"
            "Tell me where and when do you want to go and i will get you the best deals.\n"
        )
        bot.land_first_page()
        bot.select_currency("USD")
        bot.select_destination(input("Where do you want to go? => "))
        bot.select_dates(
            input(
                "What is the check-in date? (Please enter the date in the following format: yyyy-mm-dd) => "),
            input(
                "What is the check-out date? (Please enter the date in the following format: yyyy-mm-dd) => ")
        )
        bot.adults_select(int(input("How many people? ")))
        bot.start_search()
        bot.apply_filtrations()
        bot.refresh()  # this method is a workaround to give the bot time to perform the next method probarly
        bot.reporting_results()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
