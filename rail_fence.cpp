/*
ANANYA GAUTAM
2020AAPS2096H
*/

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

string rail_char(vector<vector<char>> square, string ct)
{
    int c = square[0].size();
    int m = square.size();
    int i = 0, f = 0;
    for (int j = 0; j < c; j++)
    {
        square[i][j] = '$';
        if (i == m - 1)
        {
            f = 1;
        }
        else if (i == 0)
        {
            f = 0;
        }
        if (f == 0)
        {
            i++;
        }
        else
        {
            i--;
        }
    }

    int k = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (square[i][j] == '$')
            {
                square[i][j] = ct[k++];
            }
        }
    }
    i = 0;
    f = 0;
    k = 0;
    for (int j = 0; j < c; j++)
    {
        ct[k++] = square[i][j];
        if (i == m - 1)
        {
            f = 1;
        }
        else if (i == 0)
        {
            f = 0;
        }
        if (f == 0)
        {
            i++;
        }
        else
        {
            i--;
        }
    }
    return ct;
}

vector<string> rail_word(vector<vector<string>> square, vector<string> word)
{
    int c = square[0].size();
    int m = square.size();
    int i = 0, f = 0;
    for (int j = 0; j < c; j++)
    {
        square[i][j] = "$";
        if (i == m - 1)
        {
            f = 1;
        }
        else if (i == 0)
        {
            f = 0;
        }
        if (f == 0)
        {
            i++;
        }
        else
        {
            i--;
        }
    }

    int k = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (square[i][j] == "$")
            {
                square[i][j] = word[k++];
            }
        }
    }
    i = 0;
    f = 0;
    k = 0;
    for (int j = 0; j < c; j++)
    {
        word[k++] = square[i][j];
        if (i == m - 1)
        {
            f = 1;
        }
        else if (i == 0)
        {
            f = 0;
        }
        if (f == 0)
        {
            i++;
        }
        else
        {
            i--;
        }
    }
    return word;
}
vector<string> remove(vector<string> word, string x, int c, string ct)
{
    int id;
    int l = x.length();
    for (int i = 0; i < c;)
    {
        id = ct.find(x, i);
        string s = "";
        if (id == string::npos)
        {
            while (i < c)
            {
                s += ct[i];
                i++;
            }
        }
        else
        {
            while (i < id)
            {
                s += ct[i];
                i++;
            }
            i += l;
        }
        word.push_back(s);
    }
    return word;
}
int main()
{
    // Write your code here
    int N, n, M, m;
    cin >> N >> n >> M >> m;
    string x, ct;
    cin >> x >> ct;
    int c = ct.length();

    vector<vector<char>> square(m, vector<char>(c, ' '));
    while (M--)
    {
        ct = rail_char(square, ct);
    }
    vector<string> word;
    word = remove(word, x, c, ct);
    int w = word.size();

    vector<vector<string>> square2(n, vector<string>(w, " "));
    while (N--)
    {
        word = rail_word(square2, word);
    }
    for (int i = 0; i < w; i++)
    {
        cout << word[i] << " ";
    }
    return 0;
}