#include <iostream>
#include <fstream>
#include <string>
#include <set>

int get_priority(char letter)
{
	if ('a' <= letter && letter <= 'z')
		return (int) (letter - 'a') + 1;
	if ('A' <= letter <= 'Z')
		return (int) (letter - 'A') + 27;
	return 0;
}


int main(int argc, char* argv[])
{
	std::ifstream file;
	file.open(argv[1]);
	if (!file.is_open())
		return 0;
	std::string line;
	int priorities_sum = 0;
	std::set<char> left_compartment;
	std::set<char> right_compartment;
	while (getline(file, line)) {
		for (int i = 0; i <= line.length()/2; i++)
		{
			char left_letter = line[i];
			char right_letter = line[line.length()-1-i];
			if (right_compartment.find(left_letter) != right_compartment.end())
			{
				priorities_sum += get_priority(left_letter);
				break;
			}
			left_compartment.insert(left_letter);
			if (left_compartment.find(right_letter) != left_compartment.end())
			{
				priorities_sum += get_priority(right_letter);
				break;
			}
			right_compartment.insert(right_letter);
		}
		left_compartment.clear();
		right_compartment.clear();
	}
	file.close();
	std::cout << priorities_sum << std::endl;
	return 0;
}
