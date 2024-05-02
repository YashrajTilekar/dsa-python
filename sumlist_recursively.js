const sumRecursively = (numList ,i ,N ,sum) => {
    if(i === N){    
        return sum;
    }
    else{
        return sumRecursively(numList ,i+1 ,N ,sum + numList[i]);
    }
}

const main = () => {
    const Data = [10 ,20 ,50 ,100];
    const ret = sumRecursively(Data ,0 ,Data.length ,0);

    console.log(ret);
}

main()