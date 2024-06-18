import os
import time
import openai

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


# def call_openai(
def call_gpt_model(
    context_messages: list[dict],
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.2,
    # max_tokens=256,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
) -> str:
    """https://platform.openai.com/docs/guides/chat/introduction"""
    content = ""
    try:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=context_messages,
        )
        content = response.choices[0].message.content
    except openai.BadRequestError as e:
        print(f"Error 400: {e}")
    except openai.AuthenticationError as e:
        print(f"Error 401: {e}")
    except openai.PermissionDeniedError as e:
        print(f"Error 403: {e}")
    except openai.NotFoundError as e:
        print(f"Error 404: {e}")
    except openai.UnprocessableEntityError as e:
        print(f"Error 422: {e}")
    except openai.RateLimitError as e:
        print(f"Error 429: {e}")
    except openai.InternalServerError as e:
        print(f"Error >=500: {e}")
    except openai.APIConnectionError as e:
        print(f"API connection error: {e}")
    return content


def create_message(role: str, content: str) -> dict[str, str]:
    return {"role": role, "content": content.strip()}


def create_message_from_template(template: str) -> dict[str, str]:
    content = template
    return create_message("user", content)


def main():
    # context_messages = [
    #     create_message("system", "You are ChatGPT."),
    #     create_message("user", "Marco."),
    # ]
    # content = call_gpt_model(context_messages)
    # context_messages.append(create_message("assistant", content))
    # print(context_messages)

    text = "South Africa Re-Elects Cyril Ramaphosa of the ANC as President: South African president Cyril Ramaphosa of the African National Congress (ANC) party was re-elected on Friday, and will lead the country's first multi-party coalition government.\nTwo Men Charged With Running Darknet Marketplace Empire Market: Federal prosecutors in Illinois have charged two men with owning and operating Empire Market, a darknet marketplace, according to court documents filed Friday.\nMass Adoption Would Ruin Crypto. Keep It a Niche: There is an unavoidable tension between the aims of decentralization and onboarding everyday users.\nBitcoin Plunges to $65K, Altcoins Bleed 10%-20% as Week Turns Ugly: BTC plummeted more than 2% in an hour to $65,200 during the U.S. trading session from around the $67,000 area. The leading crypto was down 7.5% over the past seven days\nMicroStrategy Increases Convertible Note Offering by 40% to $700M in Bitcoin Splurge: The proceedings of the issuance will be used to acquire more bitcoin and for general corporate affairs.\nDrake on Brink of $1M Bitcoin Loss as NHL and NBA Bets Sour: Canadian singer Drake is on the cusp of losing $1 million worth of crypto after he placed two individual $500,000 bets on the Edmonton Oilers and the Dallas Mavericks to win their respective Stanley Cup and NBA finals.\nDeFi Heavyweight Curve Focused on Becoming ‘Safest’ Lending Platform, Founder Says: Curve founder Michael Egorov’s $100 million in loans taken from various protocols using Curve’s CRV tokens started to automatically liquidate on Thursday, sending the token down as much as 30% before it briefly recovered.\nFirst Mover: Bitcoin Struggles Near $67,000 as Cryptos Lag Behind Stocks: The latest price moves in bitcoin (BTC) and crypto markets in context for June 14, 2024. First Mover is CoinDesk’s daily newsletter that contextualizes the latest actions in the crypto markets.\nNigeria Drops Tax Charges Against Binance Executives: The executives, Tigran Gambaryan and Nadeem Anjarwalla, are still named in a money-laundering case.\nBitcoin Traders See Short-Term Bearish Target at $60K as Miners Pare Holdings: Persistent testing of the lows sets the bears up for quick success with their next target at $60,000, one trader said.\nMore Central Banks Are Exploring a CBDC, BIS Survey Finds: There's a greater chance of a wholesale CBDC being issued within six years than a retail one, according to the report.\nTaiwan Crypto Advocacy Body Becomes Formally Active With 24 Entities: Taiwan's crypto advocacy body, the Taiwan Virtual Asset Service Provider Association, has been formally established and the founding meeting held with 24 cryptocurrency-related entities.\nHere's Why Bitcoin's Not Keeping Pace With Nasdaq: Bitcoin has declined 6% in one week even as Nasdaq rallies to fresh record highs.\nBitcoin Could Hit $1M Within 10 Years, Bernstein Says as It Initiates Coverage of MicroStrategy: The broker initiated coverage of the stock with an outperform rating and a $2,890 price target.\nBitcoin ETFs See $226M Outflows Led by Fidelity’s FBTC: BlackRock’s IBIT was the only ETF posting a net inflow on Thursday, while most of the funds recorded outflows.\nFormer Goldman Sachs Exec Joins Anchorage Digital Bank’s Board of Directors: Crypto custody firm Anchorage Digital has added Connie Shoemaker, a former Goldman Sachs executive, to its board of directors.\nU.S. Judge Signs Off on $4.5B Terraform-Do Kwon Settlement With SEC: The settlement bans Kwon and Terraform Labs from buying and selling crypto asset securities while agreeing to pay $4.5 billion in disgorgement, prejudgement interest, and civil penalties.\nHLG Down Over 60% as Exploiter Mints 1 Billion New Tokens: The team behind the Holograph (HLG) said they have patched the exploit and is working with centralized exchanges to freeze accounts affiliated with the exploiter\nAssured Spot Ether ETF Approval Fails to Stir Slumping Crypto Market: SEC Chair Gary Gensler said he expected the new vehicles to have won full approval by the end of the summer.\nCrypto for Advisors: Advisors and Crypto: In today's Crypto for Advisors newsletter, Adam Blumberg shares the key highlights and trends from the recent FA/RIA at the Consensus 2024 conference.\nBefore Meme Stocks, WallStreetBets Traders Mainlined Options: \nBitcoin Mining Stabilizes Power Grids Strained by AI Data Centers: Bitcoin miners help expand the use of renewable energy and balance energy networks, says Ryan Condron, co-founder of Lumerin.\nEU Body Publishes Final Draft Technical Standards for Prudential Matters: MiCA: The European Banking Authority (EBA) published on Thursday the final draft technical standards on prudential matters for firms to comply with that fall under the markets in crypto assets (MICA) legislation.\nBiden’s Nonsensical Proposed 30% Tax Would Kill Bitcoin Mining in the U.S.: \nEther ETFs Should Be Fully Approved by September, Says SEC Chair Gensler: U.S. Securities and Exchange Commission Chair Gary Gensler said that the final approvals for exchange-traded funds (ETFs) trading Ethereum's ether {{ETH}} should be finished this summer, he told senators in a budget hearing on Thursday.\nSwiss Regulator Shutters Crypto-Linked FlowBank, Begins Bankruptcy Process: FINMA announced Thursday that FlowBank’s minimum capital requirements were found to have been “significantly and seriously breached.”\nEarly Buyers of Andrew Tate’s DADDY Meme Coin Apparently Sitting on $45M in Unrealized Value: There is no evidence to show Tate sold tokens from his doxxed wallets, but some supposed “insider” buying activity before the token’s promotion on X shows too much of the token in too little hands.\nWhite House Expected to Nominate CFTC Commissioners to FDIC, Treasury Roles: Reports: The White House is expected to nominate Commissioner Christy Goldsmith Romero as the next Federal Deposit Insurance Corporation Chair media outlets have reported.\nIn Defense of Fundamental Analysis Amid Memecoin Mania: Engaging in memecoin markets without thorough analysis and a clear understanding of the risks involved is effectively gambling, not investing, says Jupiter Zheng, partner at HashKey Capital.\nCrypto Markets Have Seen $12B of Net Inflows This Year, JPMorgan Says: Most of the $16 billion inflow into spot bitcoin ETFs since their launch likely came from existing digital wallets on exchanges, the report said.\nBlockchains Are Revolutionizing Public Goods Funding: Rewriting how capital flows through society is arguably the biggest unlock in crypto. As blockchains compete for market share, we’re begging to see rapid experimentation with novel forms of funding that grow ecosystems, says Sophia Dew.\nConsensys Helps Decentralize Hollywood With Film.io and VillageDAO Partnership: Film.io is the first partner to join VillageDAO, a smart contract framework and service provider for Web3 communities.\nNEAR Foundation Forms Nuffle Labs With $13M in Funding: The spinout is aimed at advancing NEAR's modularity and bringing more decentralized development to the ecosystem.\nFirst Mover Americas: Bitcoin Holds $67K, CRV Slides: The latest price moves in bitcoin (BTC) and crypto markets in context for June 13, 2024. First Mover is CoinDesk’s daily newsletter that contextualizes the latest actions in the crypto markets.\nAustralia's Treasury to Include Stablecoin Rules in Crypto Bill Draft, ASIC's Warning For Crypto Entities: Australia's regulators have provided rare updates on their plans for the digital assets sector, including plans to introduce a draft framework for stablecoins and hinted that more enforcement is on its way against unlicensed entities during an event in Sydney on Wednesday.\nMicroStrategy Proposes $500M Convertible Notes to Boost Bitcoin Stash: \nProtocol Village: Manta Foundation Launches $50M EcoFund and Ecosystem Grant Program: The latest in blockchain tech upgrades, funding announcements and deals. For the period of June 13-19.\nPaxos Cuts 20% of Staff: Reports: Bloomberg report says the company will have an increased focus on tokenization.\nERCOT CEO: Texas' Power Grid Needs Larger Increase Than Expected to Handle AI, Bitcoin Mining: The Electric Reliability Council of Texas' CEO said in Senate testimony that the state's grid capacity will need to double in the next decade to handle demand, while the Lieutenant Governor of Texas says more scrutiny is coming for this industry.\nDeFi Giant Curve Roiled as Founder's Loans Get Liquidated; CRV Slides 30%: Addresses tied to Curve founder Michael Egorov are borrowing nearly $100 million in various stablecoins against $140 million in curve tokens.\nStick With Bitcoin, 10x Research Says After Fed Predicts Just One Rate Cut For 2024: ETF inflows resumed Wednesday as U.S. inflation came in lower-than-expected.\nTrump's Appeal to Bitcoin Miners Is a Wakeup Call for Crypto to Stay Apolitical: It may seem like the industry is finally getting the political support it needs. But proceed with caution.\nThe Protocol: How Optimism Filled in Its Missing Tooth: In this week's newsletter, we delve into the Ethereum layer-2 network Optimism's delivery of \"fault proofs,\" a piece of functionality that was glaringly missing even though it was at the heart of the project's security setup.\nFed Sees Just One Rate Cut This Year; Bitcoin Gives Up Session Gains: \nTerraform Labs, Do Kwon Agree to Pay SEC a Combined $4.5B in Civil Fraud Case: \nFringe to Forefront: the Institutional Embrace of Digital Assets: Bitcoin and other major assets offer unique advantages to investors seeking growth and diversification, says Jason Leibowitz.\nWhat ETF Approval Could Mean for Ethereum: The SEC’s recent decision sets Ethereum up for success in numerous new ways, says Ilan Solot, Senior Global Markets Strategist, Marex Solutions.\nBitcoin Miners Cash in on BTC Rally as Crypto Exchange Transfers Hit Two-Month High: Transfers from bitcoin {{BTC}} mining pools to exchanges reached a two-month high this week as BTC hovered around its local high $70,000.\nShould Banks Be Crime Fighters? The Hidden (and Not So Hidden) Costs: Pointlessly onerous anti-money laundering rules lead to debanking of individuals and even entire regions, just as “financial inclusion” is thrown around as a social objective. We need a viable alternative, says Noelle Acheson.\nU.S. CPI Was Flat in May, Beating Expectations; Bitcoin Rises to $69.2K: Stubbornly high inflation readings in the past months curbed rate cut expectations weighing on asset prices."
    # content = f"Classify the text into neutral, negative, or positive\nText: {text}\nSentiment:"
    content = f"Classify the text into neutral, negative, or positive regarding the trading a short or long position in the price of bitcoin\nText: {text}\nSentiment:"
    context_messages = [create_message("user", content)]
    content = call_gpt_model(context_messages)
    print(context_messages)
    print()
    print(content)


if __name__ == "__main__":
    main()
