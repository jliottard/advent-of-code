#include <iostream>
#include <fstream>
#include <string>
#include <queue>

int main(int argc, char** argv) {
	char* filename = argv[1];
	std::ifstream file;
	file.open(filename);
	std::priority_queue<int> calories;
	if (file.is_open()) {
		std::string line;
		int current_elve_calories_sum = 0;
		while (std::getline(file, line)) {
			if (line.compare("") == 0) {
				calories.push(current_elve_calories_sum);
				current_elve_calories_sum= 0;
				continue;
			}
			current_elve_calories_sum += std::stoi(line);
		}
	}
	file.close();
	int top_three_calories = 0;
	for (int i = 0; i < 3; i++) {
		top_three_calories += calories.top();
		calories.pop();
	}
	std::cout << top_three_calories << std::endl;
	return 0;
}
