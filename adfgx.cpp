#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

string adfgx_encrypt(string keyword, string str_matrix, string plain_text)
{
    string adfgx = "ADFGX";

    vector<vector<char>> poly_square;
    for (int i = 0; i < 5; i++)
    {
        poly_square.push_back(vector<char>(str_matrix.begin() + 5 * i, str_matrix.begin() + 5 * (i + 1)));
    }

    unordered_map<char, pair<int, int>> col_key_map;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            col_key_map[poly_square[i][j]] = make_pair(i, j);
        }
    }

    vector<string> codes;
    for (int i = 0; i < plain_text.length(); i++)
    {
        pair<int, int> pos = col_key_map[plain_text[i]];
        codes.push_back(string() + adfgx[pos.first] + adfgx[pos.second]);
    }

    string code_list;
    for (auto code : codes)
    {
        code_list += code;
    }

    map<int, vector<char>> dict;
    for (int i = 0; i < keyword.length(); i++)
    {
        dict[i] = vector<char>{keyword[i]};
    }

    for (int i = 0; i < code_list.length(); i++)
    {
        dict[i % keyword.length()].push_back(code_list[i]);
    }

    vector<pair<char, int>> idxs;
    for (int i = 0; i < keyword.length(); i++)
    {
        idxs.push_back(make_pair(keyword[i], i));
    }
    sort(idxs.begin(), idxs.end());

    string ciphertext;
    for (auto indices : idxs)
    {
        int index = indices.second;
        for (int i = 1; i < dict[index].size(); i++)
        {
            ciphertext += dict[index][i];
        }
    }

    return ciphertext;
}

int main()
{
    string ciphertext = adfgx_encrypt("GERMAN", "PHQGMEAYNOFDXKRCVSZWBUTIL", "ATTACK");
    cout << ciphertext << endl;
    return 0;
}
