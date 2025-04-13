// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {console} from "forge-std/console.sol";

struct ECPoint {
    uint256 x;
    uint256 y;
}

contract EC {
    // Generator point coordinates
    uint256 constant G_X = 1;
    uint256 constant G_Y = 2;

    uint256 constant CURVE_ORDER = 21888242871839275222246405745257275088548364400416034343698204186575808495617;

    function rationalAdd(ECPoint calldata A, ECPoint calldata B, uint256 num, uint256 den)
        public
        view
        returns (bool verified)
    {
        uint256 cX;
        uint256 cY;
        uint256 cX_derived;
        uint256 cY_derived;
        {
            (bool success, bytes memory result) = address(0x06).staticcall(abi.encode(A.x, A.y, B.x, B.y));
            require(success, "Invalid EC Points");
            (cX, cY) = abi.decode(result, (uint256, uint256));
        }
        // calculate mod fraction like c = e / f
        // c = e * pow(f, -1, curve_order) % curve_order
        uint256 inv = _modExp(den, CURVE_ORDER - 2, CURVE_ORDER);
        uint256 c = mulmod(num, inv, CURVE_ORDER);
        {
            (bool success, bytes memory result) = address(0x07).staticcall(abi.encode(G_X, G_Y, c));
            require(success, "C point calculation failed");
            (cX_derived, cY_derived) = abi.decode(result, (uint256, uint256));
        }
        verified = cX == cX_derived && cY == cY_derived;
    }

    function _modExp(uint256 base, uint256 exp, uint256 mod) internal view returns (uint256) {
        bytes memory precompileData = abi.encode(32, 32, 32, base, exp, mod);
        (bool ok, bytes memory data) = address(0x05).staticcall(precompileData);
        require(ok, "expMod failed");
        return abi.decode(data, (uint256));
    }
}
