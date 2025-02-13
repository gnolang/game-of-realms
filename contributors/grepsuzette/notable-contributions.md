# notable-contributions

Until the gno.land beta launch. Also visible on my asteroid [here](https://greps.gnasteroid.com/notable_contribs.md).

## Port Joeson from coffeescript to golang

Worked on this from june 2022 until january 2023. Bounty [applied for](https://github.com/gnolang/bounties-old/issues/33) on Feb 2, 2023.

    4. Port JOESON to Go
    github.com/jaekwon/joescript
    The intent is to create an independent left-recursive PEG parser for Gno.
    Optional: port Joescript or Javascript.
    1000 ATOMs from @jaekwon
    More GNOTs than from #3.

 The [port is here](https://github.com/grepsuzette/joeson/).

## GNO grammar - partial

In summer 2023, started to port the GNO grammar using Joeson. Grammar was posted in [PR 1156](https://github.com/gnolang/gno/pull/1156). There are only 3 files (in `gnovm/pkg/gnolang`), they are quite dense though:

1. [joeson_test.go](https://github.com/grepsuzette/gno/blob/joeson/gnovm/pkg/gnolang/joeson_test.go)
2. [joeson_rules.go](https://github.com/grepsuzette/gno/blob/joeson/gnovm/pkg/gnolang/joeson_rules.go)
3. [joeson_f.go](https://github.com/grepsuzette/gno/blob/joeson/gnovm/pkg/gnolang/joeson_f.go)

## gnAsteroid

gnAsteroid is an asteroid creation-kit, it was started, merely for myself, around the time came publicly posting my joeson port. 

Asteroids orbit gno.land, it's the same blockchain, but different frontend,
themable, working with wiki-like markdown files (enabling realms from gno.land
to be rendered there).

* [asteroid 0](https://gnAsteroid.com) - asteroid explaining what it is, containing instructions, to use, deploy on [Akash](https://gnasteroid.com/publishing/akash.md), [Vercel](https://gnasteroid.com/publishing/vercel.md)
* [greps' asteroid](https://greps.gnasteroid.com) - _precious_
* [gnAsteroid](https://github.com/gnasteroid/gnasteroid)

## Research with markdown and gnoweb, mini-games, experiments (summer-oct 2024)

Experiments including 2 games and **research with gnoweb, markdown, html, css, js-less**.

* https://greps.gnasteroid.com/r/grepsuzette/pr2554/v6/games/tictactoe
* https://greps.gnasteroid.com/r/grepsuzette/pr2554/v6/games/minesweeper

You can check [the page with all experiments here](https://greps.gnasteroid.com/conjects/gnoweb.md).

## Tendermint vuln retrospective (2023)

Also worked on an anthology of publicly knowned vulnerabilities that affected Tendermint. 

* [Cosmos-sdk vulnerability retrospective](https://github.com/gnolang/gno/issues/587)
* found most vulns were not affecting our Tendermint version, however:
* [demonstrated vulnerability to BSC 2022-10-07 hack](https://github.com/gnolang/gno/pull/583)
* [proposed fix to vuln to BSC 2022-10-07 hack (merged)](https://github.com/gnolang/gno/pull/584)
* not all of them were tested, as I was hoping some more feedback before to continue.

Thanks for reading!
