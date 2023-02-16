import random
import math

winners = []
rounds = 0


def lotto_numbers():
    numbers = list(range(1, 70))
    return numbers


def power_ball():
    powerBall = list(range(1, 27))
    return powerBall


def gen_ticket():
    lottoNumbers = lotto_numbers()
    powerBall = power_ball()

    temp = random.choice(lottoNumbers)
    num1 = temp
    lottoNumbers.remove(temp)
    temp = random.choice(lottoNumbers)
    num2 = temp
    lottoNumbers.remove(temp)
    temp = random.choice(lottoNumbers)
    num3 = temp
    lottoNumbers.remove(temp)
    temp = random.choice(lottoNumbers)
    num4 = temp
    lottoNumbers.remove(temp)
    temp = random.choice(lottoNumbers)
    num5 = temp
    lottoNumbers.remove(temp)
    temp = random.choice(powerBall)
    pball = temp
    powerBall.remove(temp)

    ticket = [num1, num2, num3, num4, num5, pball]
    return ticket


def run_lotto():
    global rounds
    i = 0
    lottoTickets = []
    while i != 10000000:
        currentTicket = gen_ticket()
        lottoTickets.append(currentTicket)
        i += 1
    winner = gen_ticket()

    if winner in lottoTickets:
        # print(f"We have a winner! : {winner} (round: {rounds})")
        winners.append(winner)
        rounds += 1
        return True
    else:
        rounds += 1
        print(f"No winners... (round: {rounds})")
        return False


def repeat_lotto():
    flag = 0
    while flag != 10:
        results = run_lotto()
        if results is True:
            flag += 1
            print("We got a winner!", winners)
            print("lotto odds: ", lotto_odds())

        else:
            flag = flag
            # print(f"We currently have: ", len(winners), " winners")
    print("We got a winner!")
    for winner in winners:
        print(winner)
    print("lotto odds: ", lotto_odds())


def lotto_odds():
    lottoNumbersSize = len(lotto_numbers())
    powerballSize = len(power_ball())
    lottoNumbersOdds = math.factorial(lottoNumbersSize) / ((math.factorial(5))*(math.factorial(lottoNumbersSize-5)))
    odds = lottoNumbersOdds * powerballSize
    return odds


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    repeat_lotto()
    # print(lotto_odds())