const merge = (numList, p, q, r) => {
    let subList1 = [];
    let subList2 = [];

    //Build SubList 1
    for (let Cnt = p; Cnt <= q - 1; Cnt++) {
        subList1.push(numList[Cnt]);
    }

    //Build SubList 2
    for (let Cnt = q; Cnt <= r; Cnt++) {
        subList2.push(numList[Cnt]);
    }

    let cntNumList = p;
    let Cnt1 = 0;
    let Cnt2 = 0;
    while (true) {
        if (subList1[Cnt1] <= subList2[Cnt2]) {
            numList[cntNumList] = subList1[Cnt1];
            Cnt1++;
            cntNumList++;

            if (Cnt1 >= subList1.length) {
                for (Cnt2; Cnt2 < subList2.length; Cnt2++, cntNumList++) {
                    numList[cntNumList] = subList2[Cnt2];
                }
                break;
            }
        }
        else {
            numList[cntNumList] = subList2[Cnt2];
            Cnt2++;
            cntNumList++;

            if (Cnt2 >= subList2.length) {
                for (Cnt1; Cnt1 < subList1.length; Cnt1++, cntNumList++) {
                    numList[cntNumList] = subList1[Cnt1]
                }
                break;
            }
        }
    }

    return numList
}

const main = () => {
    const data = [123, 245, 343, 10, 20, 30, 40, 50, 15, 17, 25, 6786, 4423];
    const retList = merge(data, 3, 8, 10)

    console.log(retList)
}

main()