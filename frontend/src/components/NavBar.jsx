import React from "react";
import Logo from "./Logo";
import SearchBar from "./SearchBar";
import Accounts from "./Accounts";

const NavBar = () => {
  return (
    <div className="flex flex-row justify-between items-center border-b-2 border-orange-300">
        <Logo />
        <SearchBar />
        <Accounts />
    </div>
  );
};

export default NavBar;
