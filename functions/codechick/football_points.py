# https://codechick.io/challenges/29

def football_points(wins, draws, losses):
    total_wins = 3 * wins
    total_draws = 1 * draws
    total_losses = 0 * losses
    # total_draws = draws
    # total_losses = 0

    total_sum = total_wins + total_draws + total_losses
    return total_sum


res_one = football_points(5, 0, 2)
print(res_one)
