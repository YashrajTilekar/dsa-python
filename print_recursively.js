/**
 * 
 * @param {Lsit of Integers} numList 
 * @param {Lerngth of numList} N 
 * @param {*} i 
 * @returns 
 */
const printRecusively = (numList, N, i) => {
    if(i === N){
        return null;
    }
    else{
        console.log(`numList[${i}] : ${numList[i]}`);
        printRecusively(numList ,N ,i+1);
    }
}

const main = () => {
    const Data = [11 ,21 ,51 ,101 ,151];
    printRecusively(Data ,Data.length ,0);
    console.log("END");
}

main()