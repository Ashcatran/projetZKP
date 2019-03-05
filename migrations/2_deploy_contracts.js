const verifier = artifacts.require("Verifier.sol")
//const migrations = artifacts.require("./Migrations.sol")

module.exports = function(deployer) {
	deployer.deploy(verifier);
};
