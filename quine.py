quine = "quine = " + chr(34) + " + chr(34)print(quine[0:9] + quine[0:9] + quine[9:19] + quine[9:12] + quine[8:] + quine[8:9] + chr(10) + quine[19:])"
print(quine[0:9] + quine[0:9] + quine[9:19] + quine[9:12] + quine[8:] + quine[8:9] + chr(10) + quine[19:])
