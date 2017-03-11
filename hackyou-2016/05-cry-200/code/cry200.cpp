#include <iostream>
#include <vector>
int main() {
	int i;
	char string[6];
	int row1[] = {2, 4, 1, 3, 6, 5};
	int row2[] = {3, 1, 4, 2, 6, 5};
	int row3[] = {6, 4, 5, 3, 1, 2};
	int row4[] = {6, 1, 4, 5, 2, 3};
	int row5[] = {3, 5, 1, 6, 4, 2};
	char secret[] = "secret";
	std::cin >> string; 
	std::vector<char> tmp, out;
	tmp.resize(6);
	out.resize(6);
	copy(string, string + 6, tmp.begin());
	for (i = 0; i < 6; i += 1) {
		out[row1[i] - 1] = tmp[i] ^ secret[i];
	}
	tmp = out;
	for (i = 0; i < 6; i += 1) {
		out[row2[i] - 1] = tmp[i] ^ secret[i];
	}
	tmp = out;
	for (i = 0; i < 6; i += 1) {
		out[row3[i] - 1] = tmp[i] ^ secret[i];
	}
	tmp = out;
	for (i = 0; i < 6; i += 1) {
		out[row4[i] - 1] = tmp[i] ^ secret[i];
	}
	tmp = out;
	for (i = 0; i < 6; i += 1) {
		out[row5[i] - 1] = tmp[i] ^ secret[i];
	}
	for (i = 0; i < 6; i += 1) {
		std::cout << int(out[i]) << std::endl;
	}
}
