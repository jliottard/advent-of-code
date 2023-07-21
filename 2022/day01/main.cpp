#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char** argv) {
	int max = 0;
	int sum = 0;
	char* filename = argv[1];
	std::ifstream file;
	file.open(filename);
	if (file.is_open()) {
		std::string line;
		while (std::getline(file, line)) {
			if (line.compare("") == 0) {
				if (sum > max) {
					max = sum;
				}
				sum = 0;
				continue;
			}
			sum += std::stoi(line);
		}
	}
	file.close();
	std::cout << max << std::endl;
	return 0;
}
