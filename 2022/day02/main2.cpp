#include <iostream>
#include <fstream>

int my_outcome_score(char outcome)
{
	return (int)(outcome - 'X') * 3;
}

int my_shape_score(char shape)
{
	return (int)(shape - 'X') + 1;
}

int score(char opponent_shape, char my_outcome)
{
	int my_symbol = (int)(my_outcome - 'X');
	int opp_symbol = (int)(opponent_shape - 'A');
	int my_shape[3][3] = {
		// I lose, draw, win
		{'Z', 'X', 'Y'},	// Opponent plays Rock
		{'X', 'Y', 'Z'},	// Opponent plays Paper
		{'Y', 'Z', 'X'},	// Opponent plays Scissor
	};
	return my_outcome_score(my_outcome) + my_shape_score(my_shape[opp_symbol][my_symbol]);
}

int main(int argc, char* argv[])
{
	std::ifstream file;
	file.open(argv[1]);
	if (!file.is_open())
	{
		return 0;
	}
	std::string line;
	int total_score = 0;
	while (getline(file, line))
	{
		total_score += score(line[0], line[2]);
	}
	file.close();
	std::cout << total_score << std::endl;
	return 0;
}

