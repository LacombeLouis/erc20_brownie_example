// contracts/BocconiToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/2a09e50d09a6795b4bfdfae0075bdd5ca88e4d97/contracts/token/ERC20/ERC20.sol";

contract BocconiToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("BocconiToken", "BT") {
        _mint(msg.sender, initialSupply);
    }
}
