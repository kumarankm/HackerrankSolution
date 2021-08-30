'''
Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''

# Program
def climbingLeaderboard(ranked, player):
    final = []
    rankedd = set(ranked)
    ranked1 = list(rankedd)
    ranked1.sort(reverse = True)
    for i in player:
        ranked1.append(i)
        ranked1.sort(reverse = True)
        rank = ranked1.index(i) + 1
        final.append(rank)
    return final

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
