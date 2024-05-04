/**
 * 
 * @param {*} numList 
 * @param {*} searchData 
 * @param {*} i 
 * @param {*} N 
 * @returns Index of search Data (-1 if not found)
 */
const searchRecursively = (numList, searchData ,i ,N) => {
    if(i === N){
        return -1;
    }
    else if(numList[i] === searchData){
        console.log(i);
        return i;
    }
    else{
        return searchRecursively(numList ,searchData ,i+1 ,N);
    }
}

const main = () => {
    const Data = [11 ,21 ,51 ,101 ,151];
    const ret = searchRecursively(Data ,510 ,0 ,Data.length);
    
    console.log(ret);
    console.log("END");
}

main()