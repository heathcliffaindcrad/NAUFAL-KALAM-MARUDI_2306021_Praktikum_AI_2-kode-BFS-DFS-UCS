{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMEct5+YKNPG9C/xYQbgbVd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/heathcliffaindcrad/Praktikum_Search_Algorithms/blob/UTAMA/ucs.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IVxHsiCpNC3p",
        "outputId": "d6844c9c-d55a-4121-f1ec-b48047b3daa7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Minimum cost from 0 to 6 is = 3\n"
          ]
        }
      ],
      "source": [
        "def uniform_cost_search(goal, start):\n",
        "    global graf, cost\n",
        "    answer = []\n",
        "\n",
        "    queue = []\n",
        "\n",
        "    for i in range(len(goal)):\n",
        "        answer.append(10**8)\n",
        "\n",
        "    queue.append([0, start])\n",
        "\n",
        "    visited = {}\n",
        "\n",
        "    count = 0\n",
        "\n",
        "    while len(queue) > 0:\n",
        "        queue = sorted(queue)\n",
        "        p = queue[-1]\n",
        "        del queue[-1]\n",
        "        p[0] *= -1\n",
        "\n",
        "        if p[1] in goal:\n",
        "            index = goal.index(p[1])\n",
        "\n",
        "            if answer[index] == 10**8:\n",
        "                count += 1\n",
        "\n",
        "            if answer[index] > p[0]:\n",
        "                answer[index] = p[0]\n",
        "\n",
        "            if count == len(goal):\n",
        "                return answer\n",
        "\n",
        "        if p[1] not in visited:\n",
        "            for i in range(len(graf[p[1]])):\n",
        "                queue.append([(p[0] + cost[(p[1], graf[p[1]][i])]) * -1, graf[p[1]][i]])\n",
        "\n",
        "            visited[p[1]] = 1  # Ini harus tetap dalam blok if, tetapi return dihapus di sini\n",
        "\n",
        "    return answer  # Return answer dipindah keluar loop while\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    graf, cost = [[] for _ in range(8)], {}\n",
        "\n",
        "    graf[0].append(1)\n",
        "    graf[0].append(3)\n",
        "    graf[3].append(1)\n",
        "    graf[3].append(6)\n",
        "    graf[3].append(4)\n",
        "    graf[1].append(6)\n",
        "    graf[4].append(2)\n",
        "    graf[4].append(5)\n",
        "    graf[2].append(1)\n",
        "    graf[5].append(2)\n",
        "    graf[5].append(6)\n",
        "    graf[6].append(4)\n",
        "\n",
        "    cost[(0, 1)] = 2\n",
        "    cost[(0, 3)] = 5\n",
        "    cost[(1, 6)] = 1\n",
        "    cost[(3, 1)] = 5\n",
        "    cost[(3, 4)] = 2\n",
        "    cost[(2, 1)] = 4\n",
        "    cost[(4, 2)] = 4\n",
        "    cost[(4, 5)] = 3\n",
        "    cost[(5, 2)] = 6\n",
        "    cost[(5, 6)] = 3\n",
        "    cost[(6, 4)] = 7\n",
        "\n",
        "    goal = [6]  # Deklarasi goal sebagai list yang benar\n",
        "\n",
        "    answer = uniform_cost_search(goal, 0)\n",
        "\n",
        "    print(\"Minimum cost from 0 to 6 is =\", answer[0])\n"
      ]
    }
  ]
}