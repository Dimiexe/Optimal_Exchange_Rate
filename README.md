# Opyimal Exchange Rate

## The "problem" and its "causes"
This is a pet project of mine, which aims to detect the optimal exchange rate achievable from EUR (€) to CHF (Swiss Francs). A total of 5 curencies are involved in the searching process i.e. EUR, CHF, USD, GBP and JPY. The program is trying to find the optimal exchange path from EUR to CHF (e.g. EUR => GBP => USD => CHF). The optimal path is that with the highest rate of conversion, or simply the path that turns a given amount of EUR to the highest CHF amount possible.

The purpose of this project is 2-fold.
*1 I live in switzerland and currently I am paid in EUR as an outsourcing agent for a company in the EU.
*2 The Swiss Central Bank recently (June 2022) announced a raise to its intrest rates, that sparked a rise of CHF against the EUR.
So in light of those events, I was currious if there is a way to make the best out of my money by swaping it around, potentially benefiting from differentforeign exchange rates.

## The Code
The code is simple and is writen in python, using jupyter notebook.
The modules needed are: pandas, requests and time.

### Functionality
First, curent echange rates for the curencies are collected from an API (https://www.alphavantage.co) and stored in a pandas DataFrame.
Then, a recursive function evaluates all potential exchange rates paths, starting from EUR and ending in CHF. (This hypothesis is based on 0 comisin or any other kind of fees needed for currency echange). Finally, the program shows any paths, and their absulute gains, that scored at least 1% better performance than the base EUR=>CHF echange, as well as the most profitable path detected paired with its excange ratio.
