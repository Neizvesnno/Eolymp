#include <iostream>
#include <vector>

int main() {

    int n;
    std::cin >> n;
    std::vector<int> arr(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    int result = 1, counter_zero = 0;

    for (int i = 0; i < n; ++i) {
        if (arr[i] != 0) {
            result *= arr[i];
        }
        else
        {
            counter_zero++;
        }
    }

    for (int i = 0; i < n; ++i) {
        if (counter_zero > 1 || (arr[i] != 0 && counter_zero == 1)) {
            std::cout << 0 << " ";
        }
        else {
            if (arr[i] != 0) {
                std::cout << static_cast<int>(result / arr[i]) << " ";
            }
            else {
                std::cout << static_cast<int>(result) << " ";
            }
        }
    }

    return 0;
}
