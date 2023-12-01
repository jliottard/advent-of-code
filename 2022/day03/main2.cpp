#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <algorithm>

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
	std::string first_line, second_line, third_line;
	int priorities_sum = 0;
	std::set<char> first_set, second_set, third_set;
	while (file >> first_line >> second_line >> third_line) {
		for (int i = 0; i <= first_line.length(); i++)
			first_set.insert(first_line[i]);
		for (int i = 0; i <= second_line.length(); i++)
			second_set.insert(second_line[i]);
		for (int i = 0; i <= third_line.length(); i++)
			third_set.insert(third_line[i]);
		std::set<char> first_and_second_intersection;
		std::set_intersection(first_set.begin(), first_set.end(), second_set.begin(), second_set.end(), first_and_second_intersection);
		std::set<char> all_intersection;
		//TODO
		std::set_intersection(first_and_second_intersection.begin(), first_and_second_intersection.end(), third_set.begin(), third_set.end(), all_intersection);
        priorities_sum += get_priority(*(all_intersection.erase(all_intersection.begin())));
		first_set.clear();
		second_set.clear();
		third_set.clear();
		first_and_second_intersection.clear();
		all_intersection.clear();
	}
	file.close();
	std::cout << priorities_sum << std::endl;
	return 0;
}
