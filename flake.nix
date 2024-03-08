{
  description = "Python dev environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in with pkgs; {
        devShells.default = mkShell {
          buildInputs = [
            python311
            openssl
            nodePackages.pyright

            ruff
            ruff-lsp

            (pkgs.python311.withPackages (pyp: [ pyp.qtile pyp.qtile-extras ]))
          ];
        };
        packages.default = lights;
      });
}
