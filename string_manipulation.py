def main():
    tampa = "tampa"
    florida = "florida"

    tampa = tampa[3:5] + tampa[2]
    co = florida.find(tampa[1])
    florida = tampa + florida[co: co+1]

    print(florida) # pama

main()