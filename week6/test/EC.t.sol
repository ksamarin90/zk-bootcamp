// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {EC} from "../src/EC.sol";

contract ECTest is Test {
    EC public ec;

    function setUp() public {
        ec = new EC();
    }

    function test_balances_equation() external {}
}
