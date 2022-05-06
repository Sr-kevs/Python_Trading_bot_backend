# Binance Trading Bot

This python script is to automate the trading of funds in a cryptocurrency trading platform called Binance, for that you enable a connection to the API's that were activated and given to the user when creating a client account in the platform.

Once connection is established, you receive a live and constant flow of data which the script will be monitoring all the time, unless the machine crashes, connection is disrupted and/or user stops it.

This automation of trading can be implemented for spot or futures trading. The script shown is for futures trading.

This is a personal project, so it's unfinished at the moment only ended the back-end part for now. Trying to do the front-end.

## How to trade?

First and foremost, what we're trying to do is to do trading, so this is what we're going to automate.

#### What is trading?

Trade or trading is a basic economic concept involving the buying and selling of goods and services, with compensation paid by a buyer to a seller, or the exchange of goods or services between parties.

In this day and age trading is enabled by using a computer and the more advanced systems use supercomputers with complex AI.

## First Step

First thing to do is to know which trading strategy you want to use. In this case will do a **grid trading strategy**.

#### Grid Trading Strategy

Grid trading is an automated currency trading strategy  where an investor creates a so-called “price grid”. The basic idea of the strategy is to repeatedly buy at the pre-specified price and then wait for the price to rise above that level and then sell the position (and vice versa with shorting and covering).

![[Pasted image 20220503141708.png]]

## Second Step

Now that we know which strategy to use. WE automate the trading instead of doing it manually by a person. This comes with advantage since the cryptocurrencies markets work 24/7. Impossible to follow by a single human.

## Third Step

Right the code. Sound easy but it took me a while.

On the futures market you can buy on the long or short side, meaning, you bet with or against what you think the price movement is going to be.

For example, if you think it price is going up you bet long (betting to go alongside the price movement), so of price goes up you will gain price appreciation and when selling, the difference between price bought and sold is your gains

if you think price is going down you bet short (betting that price will be reduced), in this case if price goes down and you *"shorted"* whatever you bought, you will gain the difference between what you bought it at and what you sold. Bringing you some gains.

In case you want to get deeper in the short and long trading rabbit hole, a quick google search will give more details on the subject.

Now if you bought on the long side and short side at the same time, you don't care if it goes up or down because, if you lose on one side you gain on the other, this is called *"hedging"* or *"hedge your position"*.

This can be accomplished by using the code **marketatwill.py** found in the git repository.

Once you bought on the long and short side (this is called opening a position, or opening a long/short position).

You want to sell (also is called close a position) one side of the opened positions (could be long or short side).

Then comes a question of when to sell long/short side and once that is sold, you're no longer hedged. After that comes another question when to sell, your unprotected side (remember you're not hedged anymore), well this depends on what the user wants to do.

Actually, if you know the answers to these questions, you could be the next millionaire making money in cryptos.

The way I have configured the scripts you could change these parameters to whatever you like in percentages from 1% up/down all the way to 100% up or down taking account from the price you bought at (also called entry price).

### Script Explaining

For the script to be easy to use and modular, all are exact same copies or have snippets of same code, just changing variables for:

- Selling (on LONG side)

- Buying (on LONG side)

- Selling (on SHORT side)

- Buying (on SHORT side)

- How much to sell?

### API Information

All documentation about Binance API can be found here:

- https://binance-docs.github.io/apidocs/spot/en/#change-log

## Hypothetic situation

Since we can execute the code at whatever parameters I´m going to propose a situation to place the parameters in the code.

Let’s say I want to buy $500.00 at a certain price (open *"long"* and *"short"* positions) and if the price moves 5% percent up or down, we suppose that´s a good indication that the trend is going in that direction and that we want to sell (*"close"* the position) once the price reaches 10%.

So, we go ahead and set up our specifications on code.

1. Make that it opens position on both sides at the same time with $500.00 at the same time.  So, at our registry (Spreadsheet file called signals.xlsx) we set In out cell called **USD to buy** to the  amount to buy for the both sides  each ( meaning whatever price we set is to buy $500.00 *"long"* and $500.00 *"short"* )

![[Pasted image 20220504140701.png]]



If something does not make sense, please let me know in the comments, will be updating this document to make easier to understand