const partition = (List, p, r) => {
    let i = p - 1;
    const pivot = List[r];
    let temp = 0;

    for(let j = p ;j < r ;j++){
        if(List[j] < pivot){
            i++;
            temp = List[i];
            List[i] = List[j];
            List[j] = temp;
        }
    }

    temp = List[i+1];
    List[i+1] = List[r];
    List[r] = temp;

    return (i+1);
}

const main = () => {
    const Data = [100 ,200 ,200 ,25 ,60 ,63 ,23 ,40 ,45 ,70 ,30 ,55 ,50,1000 ,458 ,-328];
    const p = Data.indexOf(25);
    const r = Data.indexOf(50);
    
    const q = partition(Data ,p ,r);

    console.log(Data);
}

main()