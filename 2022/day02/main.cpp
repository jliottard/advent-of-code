#include <iostream>
#include <fstream>

int my_shape_score(char shape)
{
	return (int)(shape - 'X') + 1;
}

int score(char opponent_shape, char my_shape)
{
	int my_symbol = (int)(my_shape - 'X') + 1;
	int opp_symbol = (int)(opponent_shape - 'A') + 1;
	std::cout << opponent_shape << " " << my_shape << "\n";
	std::cout << opp_symbol << " " << my_symbol << std::endl;
	int outcome_score[3][3] = {
		// My Rock, Paper, Scissor
		{3, 6, 0},	// Opponent Rock
		{0, 3, 6},	// Oppenent Paper
		{6, 0, 3},	// Oppenent Scissor
	};
	return my_shape_score(my_shape) + outcome_score[opp_symbol - 1][my_symbol - 1];
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

