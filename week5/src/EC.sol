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
        ECPoint memory C = _addPoints(A, B);
        // calculate mod fraction like c = e / f
        // c = e * pow(f, -1, curve_order) % curve_order
        uint256 inv = _modExp(den, CURVE_ORDER - 2, CURVE_ORDER);
        uint256 c = mulmod(num, inv, CURVE_ORDER);

        ECPoint memory C_derived = _scalarMul(ECPoint(G_X, G_Y), c);
        verified = C.x == C_derived.x && C.y == C_derived.y;
    }

    function _modExp(uint256 base, uint256 exp, uint256 mod) internal view returns (uint256) {
        bytes memory precompileData = abi.encode(32, 32, 32, base, exp, mod);
        (bool ok, bytes memory data) = address(0x05).staticcall(precompileData);
        require(ok, "expMod failed");
        return abi.decode(data, (uint256));
    }

    function matmul(
        // elements are order per row, like:
        // [1, 2, 3, 4] => [[1, 2], [3, 4]]
        uint256[] calldata matrix,
        uint256 n,
        ECPoint[] calldata s,
        uint256[] calldata o
    ) public view returns (bool verified) {
        require(matrix.length == n * n && s.length == n && o.length == n, "Incorrect input data");
        ECPoint memory g = ECPoint(G_X, G_Y);

        ECPoint[] memory O_calculated = new ECPoint[](n);
        for (uint256 i; i < o.length; i++) {
            O_calculated[i] = _scalarMul(g, o[i]);
        }
        ECPoint[] memory O_derived = new ECPoint[](n);
        for (uint256 i; i < n; i++) {
            O_derived[i] = _rowMul(matrix, n, i, s);
        }

        for (uint256 i; i < n; i++) {
            if (!_pointsEqual(O_calculated[i], O_derived[i])) {
                return false;
            }
        }

        return true;
    }

    function _rowMul(uint256[] calldata matrix, uint256 n, uint256 row, ECPoint[] memory s)
        internal
        view
        returns (ECPoint memory rowPoint)
    {
        rowPoint = ECPoint(0, 0);
        uint256 offset = row * n;
        for (uint256 j = 0; j < n; j++) {
            uint256 scalar = matrix[offset + j];
            rowPoint = _addPoints(rowPoint, _scalarMul(s[j], scalar));
        }
    }

    function _pointsEqual(ECPoint memory A, ECPoint memory B) internal pure returns (bool) {
        return (A.x == B.x && A.y == B.y);
    }

    function _addPoints(ECPoint memory A, ECPoint memory B) internal view returns (ECPoint memory) {
        (bool success, bytes memory result) = address(0x06).staticcall(abi.encode(A.x, A.y, B.x, B.y));
        require(success, "Invalid EC Points");
        (uint256 x, uint256 y) = abi.decode(result, (uint256, uint256));
        return ECPoint(x, y);
    }

    function _scalarMul(ECPoint memory point, uint256 scalar) internal view returns (ECPoint memory) {
        (bool success, bytes memory result) = address(0x07).staticcall(abi.encode(point.x, point.y, scalar));
        require(success, "C point calculation failed");
        (uint256 x, uint256 y) = abi.decode(result, (uint256, uint256));
        return ECPoint(x, y);
    }
}
