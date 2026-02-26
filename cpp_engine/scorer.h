#ifndef SCORER_H
#define SCORER_H

#include <vector>

std::vector<float> score_vectors(
    const std::vector<float>& user,
    const std::vector<std::vector<float>>& items
);

#endif