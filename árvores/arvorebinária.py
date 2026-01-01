{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "aacf2880",
   "metadata": {},
   "source": [
    "# Árvores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a117bc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self, key):\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "        self.val = key\n",
    "\n",
    "class Btree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "    \n",
    "    def insert(self, key):\n",
    "        if self.root is None:\n",
    "            self.root = Node(key)\n",
    "        else:\n",
    "            self.\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
