''' Returns the highest scorers for given week and season'''
import argparse
from datetime import datetime


def get_current_season() -> str:
    ''' Returns the current year. '''
    current_time = datetime.now()
    return str(current_time.year)


def main(
        input_season: str, input_week: int, 
        position: str, depth: str, output: str
        ):
    ''' Entry point for weekly highest scorer. '''

    if input_season is None:
        season = get_current_season()
    else:
        season = input_season
    print(season)

    if input_week is None:
        raise ValueError("Missing week input")
    print(input_week)

    if position is None:
        selected_positions = ["QB", "RB", "WR", "TE", "K", "DEF"]
    else:
        selected_positions = [position]
    print(selected_positions)

    if depth is None:
        selected_depth = 3
    else:
        selected_depth = depth
    print(selected_depth)

    print(output)

    # TODO: Get League Data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--season', help='Enter which season')
    parser.add_argument('--week', help='Enter which week')
    parser.add_argument('--position', help='Enter which positions')
    parser.add_argument('--depth', help='Enter number of players')
    parser.add_argument('--output', default='build', help='Output path')
    args = parser.parse_args()
    main(args.season, args.week, args.position, args.depth, args.output)
