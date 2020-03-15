#!/usr/bin/python
# -*- coding: UTF-8 -*-

# class Rule:
# 	return


def main():
	filePath = "200312220407.log"

	lines = []
	with open(filePath, "r", encoding='utf-8') as fo:
		lines = fo.readlines()

	for l in lines:
		print(l.strip())


if __name__ == "__main__":
	main()