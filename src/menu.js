import React, { useEffect, useState } from "react";

const LunchMenu = () => {

    const [menuList, setMenuList] = useState([]);
    const [inputValue, setInputValue] = useState("");
    const [random, setRandom] = useState([]);


    console.log(random)


    const selectRandomMenu = () => {
        const randomIndexes = [];
        const tempList = [...menuList];
        while (randomIndexes.length < 3 && tempList.length > 0) {
            const randomIndex = Math.floor(Math.random() * tempList.length);
            randomIndexes.push(tempList[randomIndex]);
            tempList.splice(randomIndex, 1);
        }
        setRandom(randomIndexes);
    }


    const menu = (e) => {
        setInputValue(e.target.value)
    };

    const menuAddBtn = () => {
            
        fetch(`http://211.230.166.113:3333/menu-add/`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
                menu : inputValue,
            }),
        })
            .then((response) => response.json())
            .then((data) => setMenuList(data))
            .then(setInputValue(''))
        };

    useEffect(() => {
        fetch(`http://211.230.166.113:3333/menu_list/`, {
            method: "GET",
        })
            .then((response) => response.json())
            .then((data) => setMenuList(data))
    },[inputValue])

    const delMenuBtn = (e) => {
        const num = e.target.value
        fetch(`http://211.230.166.113:3333/del-menu/${num}`, {
            method:"GET"
        })
        .then((response) => response.json())
        .then((data) => setMenuList(data))
        console.log(e.target.value)
    }


    return (
        <div className="menu-container">
        <h1>오늘의 점심은 ???</h1>
        <div>
            <input
            type="text"
            value={inputValue}
            onChange={(e)=>menu(e)}
            placeholder="메뉴를 입력하세요"
            />
            <button onClick={menuAddBtn}>메뉴 추가</button>
        </div>
        <ul>
            {menuList.map((menu, index) => (
            <li key={index}>
                {menu[1]}
                <button value={menu[0]} onClick={(e)=> delMenuBtn(e)}>삭제</button>
            </li>
            ))}
        </ul>
        <button onClick={()=>selectRandomMenu()}>랜덤으로 메뉴 선택</button>
        <div id="rankings">
            <h2>가즈아!!!!!</h2>
            {random.map((menu, index) => (
                <li key={index}>{index+1}위  {menu[1]}</li>
            ))}
        </div>
        </div>
    );
};

export default LunchMenu;
