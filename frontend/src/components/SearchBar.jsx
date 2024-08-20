import React from "react";

const SearchBar = () => {
  return (
    <div>
      <input
        type="text"
        placeholder="Search anything..."
        className="m-3 py-2 px-3 border-2 border-gray-300 hover:border-orange-500 focus:outline-none focus:border-orange-500 rounded-full"
      />
    </div>
  );
};

export default SearchBar;
