#!/bin/sh

extract_frontmatter() {
    path="$1"
    sed -n '1,/---/p;1d;$d' | yq -r $path | head -n 1
}

main() {
    for contributor in contributors/*; do (
        cd $contributor
        rm -f README.md
        (
            name=""
            github_handle="$(basename $(pwd))"
            twitter_handle=""
            gnoland_username=""
            gnoland_pubkey=""
            if [ -f profile.md ]; then
                # XXX: validate profile.md (no title, html, etc)
                name=$(cat profile.md | extract_frontmatter .name)
                github_handle=$(cat profile.md | extract_frontmatter .github_handle)
                twitter_handle=$(cat profile.md | extract_frontmatter .twitter_handle)
                gnoland_username=$(cat profile.md | extract_frontmatter .gnoland_username)
                gnoland_pubkey=$(cat profile.md | extract_frontmatter .gnoland_pubkey)
            fi

            set -e
            echo "_______________________________________________________________"
            if [ ! -z "${name}" ]; then
                echo "# ${name} (${github_handle})"
            else
                echo "# ${github_handle}"
            fi

            printf "Links: "
            if [ ! -z "${github_handle}" ]; then printf "github=[@${github_handle}](https://github.com/${github_handle}) "; fi
            if [ ! -z "${gnoland_username}" ]; then printf "username=[@${gnoland_username}](https://gno.land/r/users:${gnoland_username}) "; fi
            if [ ! -z "${gnoland_pubkey}" ]; then printf "addr=${gnoland_pubkey}) "; fi
            if [ ! -z "${twitter_handle}" ]; then printf "twitter=[@${twitter_handle}](https://x.com/${twitter_handle}) "; fi
            echo

            if [ -f profile.md ]; then
                cat profile.md | \
                    sed '1{/^---$/!q;};1,/^---$/d' # remove front matter
                echo
            fi

            if [ -f notable-contributions.md ]; then
                echo "## Notable Contributions"
                cat notable-contributions.md
            fi

            # XXX: add github-contributions
            # XXX: add other sources of metrics
        ) > README.md
    ); done
}

main
