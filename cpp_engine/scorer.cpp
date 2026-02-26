#include "scorer.h"
#include <cmath>

std::vector<float> score_vectors(
    const std::vector<float>& user,
    const std::vector<std::vector<float>>& items
) {
    std::vector<float> scores;

    for (const auto& item : items) {
        float dot = 0.0;
        for (size_t i = 0; i < user.size(); i++) {
            dot += user[i] * item[i];
        }
        scores.push_back(dot);
    }

    return scores;
}